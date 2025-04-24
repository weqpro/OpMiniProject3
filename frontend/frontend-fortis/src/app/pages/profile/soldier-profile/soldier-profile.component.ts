import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { SoldierService } from '../../../services/soldier.service';
import { RouterModule, Router } from '@angular/router';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { MatTabsModule } from '@angular/material/tabs';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { FormsModule } from '@angular/forms';
import { AidRequestService } from '../../../services/aid-request.service';
import { AidRequest } from '../../../schemas/aid-request';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-soldier-profile',
  standalone: true,
  templateUrl: './soldier-profile.component.html',
  styleUrls: ['./soldier-profile.component.css'],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    RouterModule,
    FormsModule,
    MatIconModule,
    MatMenuModule,
    MatButtonModule,
    MatTabsModule,
    MatFormFieldModule,
    MatInputModule,
    MatListModule
  ]
})
export class SoldierProfileComponent implements OnInit {
  profileData: any = null;
  requests: AidRequest[] = [];
  volunteerMap: { [key: number]: any } = {};
  selectedVolunteer: any = null;
  popupVolunteerVisible: boolean = false;
  constructor(
    private fb: FormBuilder,
    private soldierService: SoldierService,
    private aidRequestService: AidRequestService,
    private router: Router,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    this.loadProfile();
    this.loadMyRequests();
  }

  loadProfile(): void {
    this.soldierService.getProfile().subscribe({
      next: (data) => {
        this.profileData = data;
      },
      error: (err) => {
        console.error('Помилка завантаження профілю:', err);
      }
    });
  }

  loadMyRequests(): void {
    this.soldierService.getProfile().subscribe({
      next: (user) => {
        this.aidRequestService.getRequestsBySoldier(user.id).subscribe({
          next: (data) => {
            this.requests = data;
            this.loadVolunteers();
          },
          error: (err) => console.error('Не вдалося завантажити запити', err)
        });
      },
      error: (err) => console.error('Не вдалося отримати користувача', err)
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

  showVolunteerPopup(volunteerId: number): void {
    this.selectedVolunteer = this.volunteerMap[volunteerId];
    this.popupVolunteerVisible = true;
  }

  closePopup(): void {
    this.popupVolunteerVisible = false;
  }

  closePopupIfOutside(event: MouseEvent): void {
    if (this.popupVolunteerVisible) {
      this.popupVolunteerVisible = false;
    }
  }

  logout(): void {
    localStorage.removeItem('access_token');
    this.router.navigateByUrl('/login', { replaceUrl: true });
  }

  editProfile(): void {
    this.router.navigate(['app-soldier-profile-edit']);
  }

  changePassword(): void {
    this.router.navigate(['app-soldier-change-password']);
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

  deleteAccount(): void {
    const confirmed = confirm('Ви впевнені, що хочете видалити обліковий запис? Цю дію неможливо скасувати.');
    if (confirmed) {
      this.soldierService.deleteAccount().subscribe({
        next: () => {
          alert('Акаунт видалено');
          localStorage.removeItem('token');
          this.router.navigate(['/login'], { replaceUrl: true });
        },
        error: (err) => {
          console.error('Не вдалося видалити акаунт', err);
          alert('Помилка при видаленні акаунту');
        }
      });
    }
  }

closeVolunteerPopup(): void {
  this.popupVolunteerVisible = false;
}

}