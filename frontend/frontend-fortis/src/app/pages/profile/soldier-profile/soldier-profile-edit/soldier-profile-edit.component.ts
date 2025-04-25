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
import { SoldierService } from '../../../../services/soldier.service';
import Swal from 'sweetalert2';

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

  constructor(
    private fb: FormBuilder,
    private soldierService: SoldierService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.profileForm = this.fb.group({
      name: ['', Validators.required],
      surname: ['', Validators.required],
      phone_number: ['', [Validators.required, Validators.pattern(/^\+380\d{9}$/)]],
      unit: [''],
      subsubunit: [''],
      battalion: [''],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });

    this.loadProfile();
  }

  loadProfile() {
    this.soldierService.getProfile().subscribe({
      next: (data) => {
        this.profileForm.patchValue({
          name: data.name,
          surname: data.surname,
          phone_number: data.phone_number,
          unit: data.unit,
          subsubunit: data.subsubunit,
          battalion: data.battalion
        });
      },
      error: (err) => {
        console.error('Помилка завантаження профілю:', err);
        Swal.fire({
          icon: 'error',
          title: 'Помилка',
          text: 'Не вдалося завантажити дані профілю.',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Гаразд',
          customClass: {
            confirmButton: 'montserrat-button'
          }
        });
      }
    });
  }

  onSubmit() {
    if (this.profileForm.invalid) return;

    const formData = this.profileForm.value;

    this.soldierService.updateProfile(formData).subscribe({
      next: () => {
        Swal.fire({
          icon: 'success',
          title: 'Профіль оновлено!',
          text: 'Дякуємо!',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Гаразд',
          customClass: {
            confirmButton: 'montserrat-button'
          }
        }).then(() => {
          this.router.navigate(['/profile/soldier']);
        });
      },
      error: (err) => {
        console.error('Помилка оновлення:', err);
        Swal.fire({
          icon: 'error',
          title: 'Помилка',
          text: 'Неправильний пароль або інша помилка.',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Гаразд',
          customClass: {
            confirmButton: 'montserrat-button'
          }
        });
      }
    });
  }

  cancel() {
    this.router.navigate(['/profile/soldier']);
  }
}
