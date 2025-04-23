import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTabsModule } from '@angular/material/tabs';
import { MatIconModule } from '@angular/material/icon';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { FormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { MatChipsModule } from '@angular/material/chips';
import {Router, RouterModule} from '@angular/router';
import {SoldierService} from '../../../services/soldier.service';
import {VolonteerService} from '../../../services/volunteer.service';
import {AidRequestService} from '../../../services/aid-request.service';
import {AidRequest} from '../../../schemas/aid-request';
import {AuthService, UserRole} from '../../../services/authentication.service';
import {HttpClient} from '@angular/common/http';


@Component({
  selector: 'app-volunteer-profile',
  standalone: true,
  templateUrl: './volunteer-profile.component.html',
  styleUrls: ['./volunteer-profile.component.css'],
  imports: [
    MatChipsModule,
    CommonModule,
    MatTabsModule,
    MatIconModule,
    MatExpansionModule,
    MatFormFieldModule,
    MatInputModule,
    MatCheckboxModule,
    MatButtonModule,
    FormsModule,
    MatMenuModule,
    RouterModule,

  ]
})
export class VolunteerProfileComponent {


  // profileData = {
  //   name: 'Андрій',
  //   surname: 'Шевченко',
  //   email: 'andrii.shevchenko@army.ua',
  //   phone_number: '+380671234567',
  //   rating:4,
  //   review:'good',
  //   description:'oaoa'
  // };
  profileData: any = null;
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
    private router: Router,
    private aidRequestService: AidRequestService,
    private volunteerService: VolonteerService,
    private authService: AuthService,
    private http: HttpClient
  ) {}


  ngOnInit(): void {
    this.volunteerService.getProfile().subscribe({
      next: (data) => {
        this.profileData = data;
        this.aidRequestService.getRequestsByVolunteer(data.id).subscribe({
          next: (requests) => {
            this.requests = requests;
            this.loadSoldiers();
          },
          error: (err) => {
            console.error('Не вдалося завантажити запити волонтера:', err);
          }
        });
      },
      error: (err) => {
        console.error('Не вдалося завантажити профіль волонтера:', err);
      }
    });
  }


  loadMyRequests(): void {
    this.aidRequestService.getAllRequests().subscribe({
      next: data => this.requests = data,
      error: err => console.error('Не вдалося завантажити запити', err)
    });
  }
  editProfile() {
    this.router.navigate(['app-volunteer-profile-edit']);
  }

  changePassword() {
    this.router.navigate(['app-volunteer-change-password']);
  }
  logout() {
    localStorage.removeItem('token');
    this.router.navigateByUrl('/login', { replaceUrl: true });
  }


  showSearch = false;
  searchQuery = '';


  toggleSearch() {
    this.showSearch = !this.showSearch;
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
