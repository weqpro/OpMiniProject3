import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AidRequestService } from '../../services/aid-request.service';
import { AuthService } from '../../services/authentication.service';
import { AidRequest } from '../../schemas/aid-request';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-request-details',
  standalone: true,
  imports: [CommonModule, MatButtonModule],
  templateUrl: './request-details.component.html',
  styleUrls: ['./request-details.component.css']
})
export class RequestDetailsComponent implements OnInit {
  request: AidRequest | null = null;
  requestId!: number;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private requestService: AidRequestService,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.requestId = Number(this.route.snapshot.paramMap.get('id'));
    this.loadRequest();
  }

  loadRequest(): void {
    this.requestService.getById(this.requestId).subscribe({
      next: data => this.request = data,
      error: err => console.error('Помилка завантаження запиту', err)
    });
  }

  acceptRequest(): void {
    this.authService.getCurrentUser().subscribe({
      next: user => {
        const volunteerId = user.id;
        this.requestService.assignToVolunteer(this.requestId, volunteerId).subscribe({
          next: () => {
            alert('Ви погодились допомогти!');
            this.router.navigate(['/my-requests-soldier']);
          },
          error: err => console.error('Помилка при підтвердженні', err)
        });
      }
    });
  }
}
