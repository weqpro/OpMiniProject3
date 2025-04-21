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

  selectedSoldier: any = null;
  popupVisible = false;
  selectedVolunteer: any = null;
  popupVolunteerVisible = false;

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


  loadVolunteers(): void {
    const ids = [...new Set(this.requests.map(r => r.volunteer_id).filter(Boolean))];
    ids.forEach(id => {
      this.http.get(`http://127.0.0.1:8000/api/v1/volunteers/${id}`).subscribe({
        next: (volunteer: any) => this.volunteerMap[id] = volunteer,
        error: err => console.error(`Не вдалося завантажити волонтера з ID ${id}`, err)
      });
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
