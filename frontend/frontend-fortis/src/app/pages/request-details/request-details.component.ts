import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AidRequestService } from '../../services/aid-request.service';
import { AuthService } from '../../services/authentication.service';
import { AidRequest } from '../../schemas/aid-request';
import { CommonModule } from '@angular/common';
import { NgIf } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-request-details',
  standalone: true,
  imports: [
    CommonModule,
    MatButtonModule,
    NgIf
  ],
  templateUrl: './request-details.component.html',
  styleUrls: ['./request-details.component.css']
})
export class RequestDetailsComponent implements OnInit {
  request: AidRequest | null = null;
  requestId!: number;
  soldierInfo: any = null;
  showPopup = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private requestService: AidRequestService,
    private authService: AuthService,
    private http: HttpClient
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

  showSoldierInfo(): void {
    if (!this.request?.soldier_id) return;

    this.http.get(`http://127.0.0.1:8000/api/v1/soldiers/soldier-info/${this.request.soldier_id}`).subscribe({
      next: data => {
        this.soldierInfo = data;
        this.showPopup = true;
      },
      error: err => console.error('Помилка при завантаженні інформації про військового', err)
    });
  }

  closePopup(): void {
    this.showPopup = false;
  }
}
