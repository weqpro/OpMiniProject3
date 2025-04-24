import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { AidRequestService } from '../../services/aid-request.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';

@Component({
  selector: 'app-edit-request',
  standalone: true,
  templateUrl: './edit-request.component.html',
  styleUrls: ['./edit-request.component.css'],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatIconModule,
    MatButtonModule,
    MatMenuModule
  ]
})
export class EditRequestComponent implements OnInit {
  requestId!: number;

  name: string = '';
  description: string = '';
  location: string = '';
  deadline: Date | null = null;
  category_id: number | null = null;

  originalData: any = {};

  cities: string[] = [
    'Київ', 'Львів', 'Харків', 'Одеса', 'Дніпро', 'Запоріжжя', 'Івано-Франківськ',
    'Чернівці', 'Ужгород', 'Тернопіль', 'Хмельницький', 'Миколаїв', 'Полтава',
    'Чернігів', 'Суми', 'Рівне', 'Житомир', 'Кропивницький', 'Черкаси', 'Вінниця'
  ];

  categories = [
    { id: 1, name: 'Автозапчастини' },
    { id: 2, name: 'Енергозабезпечення' },
    { id: 3, name: 'Генератори' },
    { id: 4, name: 'Гігієна та санітарія' },
    { id: 5, name: 'Інструменти / будматеріали' },
    { id: 6, name: 'Медицина' },
    { id: 7, name: 'Навігація' },
    { id: 8, name: 'Одяг' },
    { id: 9, name: 'Побутові послуги' },
    { id: 10, name: 'Польовий побут' },
    { id: 11, name: 'Продукти харчування' },
    { id: 12, name: 'Ремонт' },
    { id: 13, name: 'Розвідка і спостереження' },
    { id: 14, name: 'Спорядження' },
    { id: 15, name: 'Техніка' },
    { id: 16, name: 'Транспорт' },
    { id: 17, name: 'Звʼязок' }
  ];

  selectedFile: File | null = null;
  imagePreview: string | null = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private aidRequestService: AidRequestService
  ) {}

  ngOnInit(): void {
    this.requestId = Number(this.route.snapshot.paramMap.get('id'));
    this.aidRequestService.getById(this.requestId).subscribe({
      next: (data) => {
        this.originalData = data;

        this.name = data.name;
        this.description = data.description || '';
        this.location = data.location;
        this.deadline = new Date(data.deadline);
        this.category_id = data.category_id;
        this.imagePreview = data.image ? `http://127.0.0.1:8000${data.image}` : null;
      },
      error: (err) => {
        console.error('Не вдалося завантажити запит', err);
      }
    });
  }

  triggerImageInput(): void {
    document.getElementById('imageInput')?.click();
  }

  onImageSelected(event: Event): void {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (file) {
      this.selectedFile = file;
      const reader = new FileReader();
      reader.onload = () => {
        this.imagePreview = reader.result as string;
      };
      reader.readAsDataURL(file);
    }
  }
  

  saveChanges(): void {
    const payload: any = {};
  
    if (this.name.trim() !== '' && this.name.trim() !== this.originalData.name) {
      payload.name = this.name.trim();
    }
    if (this.description.trim() !== '' && this.description.trim() !== this.originalData.description) {
      payload.description = this.description.trim();
    }
    if (this.location !== '' && this.location !== this.originalData.location) {
      payload.location = this.location;
    }
    if (this.deadline && this.deadline.toISOString() !== new Date(this.originalData.deadline).toISOString()) {
      payload.deadline = this.deadline;
    }
    if (this.category_id !== null && this.category_id !== this.originalData.category_id) {
      payload.category_id = this.category_id;
    }
  
    if (this.selectedFile) {
      const formData = new FormData();
      formData.append('json_data', JSON.stringify(payload));
      formData.append('image', this.selectedFile);
  
      this.aidRequestService.updateWithImage(this.requestId, formData).subscribe({
        next: () => this.router.navigate(['/my-requests-soldier']),
        error: (err) => console.error('Помилка при збереженні змін', err)
      });
    } else {
      this.aidRequestService.updateRequest(this.requestId, payload).subscribe({
        next: () => this.router.navigate(['/my-requests-soldier']),
        error: (err) => console.error('Помилка при збереженні змін', err)
      });
    }
  }
}