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
import { Router, RouterModule } from '@angular/router';

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

  constructor(
    private router: Router,
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
        } else {
          console.error('ID волонтера не знайдено. Неможливо завантажити дані.');
        }
      },
      error: (err) => console.error('Помилка завантаження профілю:', err)
    });
  }

  loadMyRequests(volunteerId: number): void {
    this.aidRequestService.getRequestsByVolunteer(volunteerId).subscribe({
      next: (data) => this.requests = data,
      error: (err) => console.error('Помилка завантаження запитів', err)
    });
  }

  loadReviews(volunteerId: number): void {
    this.reviewService.getReviewsByVolunteer(volunteerId).subscribe({
      next: (data) => this.reviews = data,
      error: (err) => console.error('Помилка завантаження відгуків', err)
    });
  }

  editProfile(): void {
    this.router.navigate(['app-volunteer-profile-edit']);
  }

  changePassword(): void {
    this.router.navigate(['app-volunteer-change-password']);
  }

  logout(): void {
    localStorage.removeItem('access_token');
    this.router.navigateByUrl('/login', { replaceUrl: true });
  }

  toggleSearch(): void {}
}