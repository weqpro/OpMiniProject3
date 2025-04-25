import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { VolonteerService } from '../../../services/volunteer.service';
import { MatMenuModule } from '@angular/material/menu';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-volunteer-register',
  standalone: true,
  templateUrl: './volunteer-register.component.html',
  styleUrls: ['./volunteer-register.component.css'],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    MatMenuModule
  ]
})
export class VolunteerRegisterComponent {
  volunteerForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private volunteerService: VolonteerService
  ) {
    this.volunteerForm = this.fb.group({
      name: ['', Validators.required],
      surname: ['', Validators.required],
      phone_number: ['', [Validators.required, Validators.pattern(/^\+380\d{9}$/)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
    });
  }

  onSubmit(): void {
    if (this.volunteerForm.valid) {
      this.volunteerService.create(this.volunteerForm.value).subscribe({
        next: () => {
          Swal.fire({
            icon: 'success',
            title: 'Реєстрація успішна!',
            text: 'Тепер увійдіть у систему.',
            confirmButtonColor: '#39736b',
            confirmButtonText: 'Увійти'
          }).then(() => {
            this.router.navigate(['/login']);
          });
        },
        error: (err: any) => {
          console.error(err);
          Swal.fire({
            icon: 'error',
            title: 'Помилка реєстрації',
            text: 'Перевірте дані або спробуйте ще раз.',
            confirmButtonColor: '#39736b',
            confirmButtonText: 'Окей'
          });
        }
      });
    }
  }

  goToLogin(): void {
    this.router.navigate(['/login']);
  }
}
