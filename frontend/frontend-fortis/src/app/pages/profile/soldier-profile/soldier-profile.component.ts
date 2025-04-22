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
  //
  // };


  profileForm!: FormGroup;
  showSearch = false;
  searchQuery = '';

  constructor(
    private fb: FormBuilder,
    private soldierService: SoldierService,
    private router: Router
  ) {
  }

  ngOnInit(): void {
    this.loadProfile();
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
}
