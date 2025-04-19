import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { AidRequest } from '../../schemas/aid-request';
import { AidRequestService } from '../../services/aid-request.service';
import { AuthService, UserRole } from '../../services/authentication.service';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { RouterModule } from '@angular/router';
@Component({
  selector: 'app-my-requests',
  standalone: true,
  imports: [CommonModule, MatButtonModule, MatIconModule, MatMenuModule,  RouterModule],
  templateUrl: './my-request-soldier.component.html',
  styleUrls: ['./my-request-soldier.component.css']
})
export class MyRequestsComponent implements OnInit {
  requests: AidRequest[] = [];
  userRole: UserRole | null = null;

  constructor(
    private aidRequestService: AidRequestService,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.authService.getCurrentUser().subscribe({
      next: (user) => {
        this.userRole = user.role;

        if (user.role === 'soldier') {
          this.aidRequestService.getRequestsBySoldier(user.id).subscribe({
            next: data => this.requests = data,
            error: err => console.error('Не вдалося завантажити запити військового', err)
          });
        } else if (user.role === 'volunteer') {
          this.aidRequestService.getRequestsByVolunteer(user.id).subscribe({
            next: data => this.requests = data,
            error: err => console.error('Не вдалося завантажити запити волонтера', err)
          });
        }
      },
      error: err => {
        console.error('Не вдалося отримати користувача', err);
      }
    });
  }
}
