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
  profileData: any = null;
  showSearch = false;
  searchQuery = '';

  constructor(
    private fb: FormBuilder,
    private volunteerService: VolonteerService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.profileForm = this.fb.group({
      name: ['', Validators.required],
      surname: ['', Validators.required],
      phone_number: ['', [Validators.required, Validators.pattern(/^\+380\d{9}$/)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
    

    this.loadProfile();
  }

  loadProfile(): void {
    this.volunteerService.getProfile().subscribe({
      next: (data) => {
        this.profileData = data;

        this.profileForm.patchValue({
          name: data.name,
          surname: data.surname,
          phone_number: data.phone_number,
          email: data.email
        });
        
      },
      error: (err) => {
        console.error('Помилка завантаження профілю:', err);
      }
    });
  }

  onSubmit(): void {
    const formValue = this.profileForm.value;
    const payload: any = {};
  
    if (formValue.name.trim() !== this.profileData.name) {
      payload.name = formValue.name.trim();
    }
  
    if (formValue.surname.trim() !== this.profileData.surname) {
      payload.surname = formValue.surname.trim();
    }
  
    if (formValue.phone_number !== this.profileData.phone_number) {
      payload.phone_number = formValue.phone_number;
    }
  
    if (!formValue.password) {
      alert('Введіть поточний пароль');
      return;
    }
    payload.password = formValue.password;

    if (Object.keys(payload).length === 1 && payload.password) {
      this.router.navigate(['/profile/volunteer']);
      return;
    }
  
    this.volunteerService.updateProfile(payload).subscribe({
      next: () => {
        alert('Профіль оновлено');
        this.router.navigate(['/profile/volunteer']);
      },
      error: (err) => {
        console.error('Помилка оновлення:', err);
        alert('Неправильний пароль або інша помилка');
      }
    });
  }
  

  toggleSearch(): void {
    this.showSearch = !this.showSearch;
  }

  logout(): void {
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
  }

  cancel(): void {
    this.router.navigate(['/profile/volunteer']);
  }
}