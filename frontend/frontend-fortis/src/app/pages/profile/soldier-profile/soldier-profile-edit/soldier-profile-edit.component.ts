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
import {SoldierService} from '../../../../services/soldier.service';

@Component({
  selector: 'app-soldier-profile-edit',
  standalone: true,
  templateUrl: './soldier-profile-edit.component.html',
  styleUrls: ['./soldier-profile-edit.component.css'],
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
export class SoldierProfileEditComponent implements OnInit {
  profileForm!: FormGroup;
  showSearch = false;
  searchQuery = '';

  constructor(
    private fb: FormBuilder,
    private soldierService: SoldierService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.profileForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      phone: [''],
      unit: [''],
      subunit: ['']
    });

    this.loadProfile();
  }

  loadProfile() {
    this.soldierService.getProfile().subscribe({
      next: (data) => {
        this.profileForm.patchValue(data);
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
    this.router.navigate(['/login']);
  }
}
