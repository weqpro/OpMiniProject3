import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatChipsModule } from '@angular/material/chips';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { FormsModule } from '@angular/forms';
import { ReviewService } from '../../services/review.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-review',
  standalone: true,
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.css'],
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatChipsModule,
    MatIconModule,
    MatButtonModule,
    MatMenuModule,
  ]
})
export class ReviewComponent implements OnInit {
  review_text = '';
  rating = 0;
  tags: string[] = [];
  selectedTags: string[] = [];

  request_id!: number;

  positiveTags = ['швидко', 'якісно', 'вчасно', 'завжди на зв’язку', 'приємне спілкування'];
  negativeTags = ['повільно', 'неякісно', 'не вийшов на звʼязок', 'невчасно'];

  constructor(
    private reviewService: ReviewService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const idParam = params.get('id');
      if (idParam) {
        this.request_id = +idParam;
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Помилка!',
          text: 'Не знайдено ID запиту!',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Окей'
        });
      }
    });
  }

  setRating(star: number): void {
    this.rating = star;
    this.tags = star >= 4 ? [...this.positiveTags] : [...this.negativeTags];
    this.selectedTags = [];
  }

  updateSelectedTags(event: any): void {
    this.selectedTags = event.value;
  }
  
  submit(): void {
    if (!this.review_text.trim() || !this.rating || !this.request_id) {
      Swal.fire({
        icon: 'warning',
        title: 'Увага!',
        text: 'Всі поля обовʼязкові для заповнення!',
        confirmButtonColor: '#39736b',
        confirmButtonText: 'Окей'
      });
      return;
    }
  
    this.reviewService.createReview({
      review_text: this.review_text,
      rating: this.rating,
      tags: this.selectedTags,
      request_id: this.request_id,
    }).subscribe({
      next: () => {
        Swal.fire({
          icon: 'success',
          title: 'Успішно!',
          text: 'Відгук опубліковано! Дякуємо!',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Повернутись до профілю'
        }).then(() => {
          this.router.navigate(['/profile/soldier']);
        });
      },
      error: err => {
        if (err?.error?.detail === 'Review already exists for this request') {
          Swal.fire({
            icon: 'warning',
            title: 'Відгук уже існує',
            text: 'Неможливо залишити повторний відгук для цього запиту.',
            confirmButtonColor: '#39736b',
            confirmButtonText: 'Повернутись'
          }).then(() => {
            this.router.navigate(['/profile/soldier']);
          });
        } else {
          console.error(err);
          Swal.fire({
            icon: 'error',
            title: 'Помилка',
            text: 'Сталася помилка під час створення відгуку. Спробуйте ще раз!',
            confirmButtonColor: '#39736b',
            confirmButtonText: 'Окей'
          });
        }
      }
    });
  }
}
