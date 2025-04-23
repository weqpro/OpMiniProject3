import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
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

import { VolonteerService } from '../../../../services/volunteer.service';

@Component({
  selector: 'app-volunteer-profile-edit',
  standalone: true,
  templateUrl: './volunteer-profile-edit.component.html',
  styleUrls: ['./volunteer-profile-edit.component.css'],
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
    MatListModule
  ]
})
export class VolunteerProfileEditComponent implements OnInit {
  profileForm!: FormGroup;
  showSearch = false;
  searchQuery = '';

  constructor(
    private fb: FormBuilder,
    private volunteerService: VolonteerService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.profileForm = this.fb.group({
      name: [''],
      surname: [''],
      phone_number: [''],
      password: ['', Validators.required]
    });

    this.loadProfile();
  }
  profileData: any = null;
  // profileData = {
  //   name: 'Андрій',
  //   surname: 'Шевченко',
  //   email: 'andrii.shevchenko@army.ua',
  //   phone_number: '+380671234567',
  // };
  loadProfile() {
    this.volunteerService.getProfile().subscribe({
      next: (data) => {
        this.profileData = data;
      },
      error: (err) => {
        console.error('Помилка завантаження профілю:', err);
      }
    });
  }

  onSubmit() {
    const formData = this.profileForm.value;

    this.volunteerService.updateProfile(formData).subscribe({
      next: () => {
        alert('Профіль оновлено');
        this.router.navigate(['/profile/soldier']);
      },
      error: (err) => {
        console.error('Помилка оновлення:', err);
        alert('Неправильний пароль або інша помилка');
      }
    });
  }

  toggleSearch() {
    this.showSearch = !this.showSearch;
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
  }
  cancel(){
    this.router.navigate(['profile/volunteer']);
  }
}
