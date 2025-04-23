import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { AidRequest } from '../../schemas/aid-request';
import { AidRequestService } from '../../services/aid-request.service';
import { AuthService, UserRole } from '../../services/authentication.service';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { RouterModule } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-my-requests',
  standalone: true,
  imports: [CommonModule, MatButtonModule, MatIconModule, MatMenuModule, RouterModule],
  templateUrl: './my-request-soldier.component.html',
  styleUrls: ['./my-request-soldier.component.css']
})
export class MyRequestsComponent implements OnInit {
  requests: AidRequest[] = [];
  userRole: UserRole | null = null;
  volunteerMap: { [key: number]: any } = {};
  soldierMap: { [key: number]: any } = {};

  selectedSoldier: any = null;
  popupVisible = false;

  selectedVolunteer: any = null;
  popupVolunteerVisible = false;

  selectedRequest: any = null;
  popupRequestVisible = false;

  constructor(
    private aidRequestService: AidRequestService,
    private authService: AuthService,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    this.authService.getCurrentUser().subscribe({
      next: (user) => {
        this.userRole = user.role;
        const requestLoad = user.role === 'soldier'
          ? this.aidRequestService.getRequestsBySoldier(user.id)
          : this.aidRequestService.getRequestsByVolunteer(user.id);

        requestLoad.subscribe({
          next: data => {
            this.requests = data;
            if (user.role === 'soldier') this.loadVolunteers();
            else this.loadSoldiers();
          },
          error: err => console.error('Не вдалося завантажити запити', err)
        });
      },
      error: err => console.error('Не вдалося отримати користувача', err)
    });
  }

  showRequestPopup(request: any): void {
    this.selectedRequest = request;
    this.popupRequestVisible = true;
  }

  closeRequestPopup(): void {
    this.popupRequestVisible = false;
  }

  showVolunteerPopup(volunteerId: number): void {
    this.selectedVolunteer = this.volunteerMap[volunteerId];
    this.popupVolunteerVisible = true;
  }

  closeVolunteerPopup(): void {
    this.popupVolunteerVisible = false;
  }

  showSoldierPopup(soldierId: number): void {
    this.selectedSoldier = this.soldierMap[soldierId];
    this.popupVisible = true;
  }

  closePopup(): void {
    this.popupVisible = false;
  }

  closePopupIfOutside(event: MouseEvent): void {
    if (this.popupVisible) this.popupVisible = false;
    if (this.popupVolunteerVisible) this.popupVolunteerVisible = false;
    if (this.popupRequestVisible) this.popupRequestVisible = false;
  }

  markAsCompleted(requestId: number): void {
    this.aidRequestService.completeRequest(requestId).subscribe({
      next: () => {
        this.authService.getCurrentUser().subscribe({
          next: (user) => {
            const reload$ = user.role === 'soldier'
              ? this.aidRequestService.getRequestsBySoldier(user.id)
              : this.aidRequestService.getRequestsByVolunteer(user.id);

            reload$.subscribe({
              next: (data) => {
                this.requests = data;
                if (user.role === 'soldier') this.loadVolunteers();
                else this.loadSoldiers();
              },
              error: (err) => console.error('Помилка при оновленні запитів', err)
            });
          }
        });
      },
      error: err => console.error('Помилка при завершенні запиту', err)
    });
  }

  loadVolunteers(): void {
    const ids = [...new Set(this.requests.map(r => r.volunteer_id).filter(Boolean))];
    ids.forEach(id => {
      this.http.get(`http://127.0.0.1:8000/api/v1/volunteers/${id}`).subscribe({
        next: (volunteer: any) => this.volunteerMap[id] = volunteer,
        error: err => console.error(`Не вдалося завантажити волонтера з ID ${id}`, err)
      });
    });
  }

  deleteRequest(requestId: number): void {
    if (!confirm('Ви впевнені, що хочете видалити цей запит?')) {
      return;
    }
  
    this.aidRequestService.deleteRequest(requestId).subscribe({
      next: () => {
        this.requests = this.requests.filter(r => r.id !== requestId);
      },
      error: err => {
        console.error('Помилка при видаленні запиту', err);
        alert('Не вдалося видалити запит');
      }
    });
  }
  

  loadSoldiers(): void {
    const ids = [...new Set(this.requests.map(r => r.soldier_id).filter(Boolean))];
    ids.forEach(id => {
      this.http.get(`http://127.0.0.1:8000/api/v1/soldiers/soldier-info/${id}`).subscribe({
        next: (soldier: any) => this.soldierMap[id] = soldier,
        error: err => console.error(`Не вдалося завантажити військового з ID ${id}`, err)
      });
    });
  }
}
