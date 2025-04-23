import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { SoldierService } from '../../../services/soldier.service';
import { RouterModule, Router } from '@angular/router';

import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatTabsModule } from '@angular/material/tabs';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { FormsModule } from '@angular/forms';
import {MatProgressSpinner} from '@angular/material/progress-spinner';
import {AidRequestService} from '../../../services/aid-request.service';
import {AidRequest} from '../../../schemas/aid-request';
import {AuthService, UserRole} from '../../../services/authentication.service';
import {HttpClient} from '@angular/common/http';

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
    MatExpansionModule,
    MatTabsModule,
    MatFormFieldModule,
    MatInputModule,
    MatListModule,
    MatProgressSpinner
  ]
})
export class SoldierProfileComponent implements OnInit {
  profileData: any = null;
  // profileData = {
  //   name: 'Андрій',
  //   surname: 'Шевченко',
  //   email: 'andrii.shevchenko@army.ua',
  //   phone_number: '+380671234567',
  //   unit: '80-та окрема десантно-штурмова бригада',
  //   subsubunit: '2-й взвод',
  //   battalion: '3-й батальйон',
  // };
  // requests: AidRequest[] = [
  //   {
  //     id: 1,
  //     name: 'Бронежилети для взводу',
  //     description: 'Потрібні 10 бронежилетів 4 класу захисту для щоденних бойових чергувань.',
  //     image_path: '/static/images/armor.jpg',
  //     endDate: new Date('2025-05-10'),
  //     location: 'Бахмут',
  //     status: 'in_progress',
  //     soldier_id: 101,
  //     volunteer_id: 201,
  //     category_id: 1
  //   },
  //   {
  //     id: 2,
  //     name: 'Тепловізори для нічного спостереження',
  //     description: '2 тепловізори для нічних патрулів, бажано Pulsar або аналогічні.',
  //     image_path: '/static/images/thermal.jpg',
  //     endDate: new Date('2025-05-20'),
  //     location: 'Краматорськ',
  //     status: 'pending',
  //     soldier_id: 101,
  //     volunteer_id: 0,
  //     category_id: 2
  //   },
  //   {
  //     id: 3,
  //     name: 'Рації Motorola',
  //     description: '5 комплектів Motorola DP1400 з зарядками.',
  //     image_path: '/static/images/radios.jpg',
  //     endDate: new Date('2025-06-01'),
  //     location: 'Харків',
  //     status: 'completed',
  //     soldier_id: 101,
  //     volunteer_id: 202,
  //     category_id: 3
  //   }
  // ];

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

  profileForm!: FormGroup;
  showSearch = false;

  constructor(
    private fb: FormBuilder,
    private soldierService: SoldierService,
    private aidRequestService: AidRequestService,
    private router: Router,
    private authService: AuthService,
    private http: HttpClient
  ) {
  }
  //
  // ngOnInit(): void {
  //   this.loadProfile();
  //   this.loadMyRequests();
  // }

  ngOnInit(): void {
    this.soldierService.getProfile().subscribe({
      next: (profile) => {
        this.profileData = profile;

        this.aidRequestService.getRequestsBySoldier(profile.id).subscribe({
          next: (requests) => {
            this.requests = requests;
            this.loadVolunteers();
          },
          error: (err) => {
            console.error('Не вдалося завантажити запити солдата:', err);
          }
        });
      },
      error: (err) => {
        console.error('Не вдалося завантажити профіль солдата:', err);
      }
    });
  }


  loadMyRequests(): void {
    this.aidRequestService.getAllRequests().subscribe({
      next: data => this.requests = data,
      error: err => console.error('Не вдалося завантажити запити', err)
    });
  }

  loadProfile() {
    this.soldierService.getProfile().subscribe({
      next: (data) => {
        this.profileData = data;
      },
      error: (err) => {
        console.error('Помилка завантаження профілю:', err);
      }
    });
  }

  onSubmit() {
    if (this.profileForm.valid) {
      this.soldierService.updateProfile(this.profileForm.value).subscribe({
        next: () => alert('Профіль оновлено'),
        error: (err) => {
          console.error('Помилка оновлення:', err);
          alert('Не вдалося оновити профіль');
        }
      });
    }
  }

  toggleSearch() {
    this.showSearch = !this.showSearch;
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigateByUrl('/login', { replaceUrl: true });
  }


  editProfile() {
    this.router.navigate(['app-soldier-profile-edit']);
  }

  changePassword() {
    this.router.navigate(['app-soldier-change-password']);
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
