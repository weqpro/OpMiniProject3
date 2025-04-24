import { Component, OnInit } from '@angular/core';
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
import { Router, RouterModule, ActivatedRoute } from '@angular/router';
import { VolonteerService } from '../../../services/volunteer.service';
import { AidRequestService } from '../../../services/aid-request.service';
import { ReviewService } from '../../../services/review.service';
import { AidRequest } from '../../../schemas/aid-request';
import { Review } from '../../../schemas/review';
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
    RouterModule
  ]
})
export class VolunteerProfileComponent implements OnInit {
  profileData: any = null;
  requests: AidRequest[] = [];
  reviews: Review[] = [];

  selectedSoldier: any = null;
  selectedRequest: any = null;

  popupSoldierVisible = false;
  popupRequestVisible = false;

  soldierMap: { [id: number]: any } = {};
  userRole = 'volunteer';

  selectedTabIndex = 0;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private aidRequestService: AidRequestService,
    private volunteerService: VolonteerService,
    private reviewService: ReviewService
  ) {}
  ngOnInit(): void {
    this.volunteerService.getProfile().subscribe({
      next: (data) => {
        this.profileData = data;
        if (data?.id) {
          this.loadMyRequests(data.id);
          this.loadReviews(data.id);
        }
  
        this.route.queryParams.subscribe(params => {
          if (params['tab'] === 'requests') {
            this.selectedTabIndex = 1;
          }
        });
      },
      error: (err) => console.error('Помилка завантаження профілю:', err)
    });
  }
  
  loadMyRequests(volunteerId: number): void {
    this.aidRequestService.getRequestsByVolunteer(volunteerId).subscribe({
      next: (data) => {
        this.requests = data;
        this.loadSoldiers();
      },
      error: (err) => console.error('Помилка завантаження запитів', err)
    });
  }

  loadReviews(volunteerId: number): void {
    this.reviewService.getReviewsByVolunteer(volunteerId).subscribe({
      next: (data) => this.reviews = data,
      error: (err) => console.error('Помилка завантаження відгуків', err)
    });
  }

  loadSoldiers(): void {
    const ids = [...new Set(this.requests.map(r => r.soldier_id).filter(Boolean))];
    ids.forEach(id => {
      this.volunteerService.getSoldierById(id).subscribe({
        next: soldier => this.soldierMap[id] = soldier,
        error: err => console.error(`Не вдалося завантажити військового з ID ${id}`, err)
      });
    });
  }
  
  showSoldierPopup(id: number): void {
    this.selectedSoldier = this.soldierMap[id];
    this.popupSoldierVisible = true;
  }

  closeSoldierPopup(): void {
    this.popupSoldierVisible = false;
  }

  showRequestPopup(request: any): void {
    this.selectedRequest = request;
    this.popupRequestVisible = true;
  }

  closeRequestPopup(): void {
    this.popupRequestVisible = false;
  }

  editProfile(): void {
    this.router.navigate(['/app-volunteer-profile-edit']);
  }

  changePassword(): void {
    this.router.navigate(['/app-volunteer-change-password']);
  }

  logout(): void {
    localStorage.removeItem('access_token');
    this.router.navigateByUrl('/login', { replaceUrl: true });
  }

  deleteAccount(): void {
    const confirmed = confirm('Ви впевнені, що хочете видалити обліковий запис?');
    if (confirmed) {
      this.volunteerService.deleteAccount().subscribe({
        next: () => {
          alert('Акаунт видалено');
          localStorage.removeItem('access_token');
          this.router.navigate(['/']);
        },
        error: (err) => {
          console.error('Не вдалося видалити акаунт', err);
          alert('Помилка при видаленні акаунту');
        }
      });
    }
  }

  markAsCompleted(requestId: number): void {
    this.aidRequestService.completeRequest(requestId).subscribe({
      next: () => {
        this.loadMyRequests(this.profileData.id);
      },
      error: (err) => {
        console.error('Помилка при завершенні запиту', err);
      }
    });
  }
}
