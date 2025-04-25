import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { SoldierService } from '../../../services/soldier.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-soldier-register',
  standalone: true,
  templateUrl: './soldier-register.component.html',
  styleUrls: ['./soldier-register.component.css'],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule
  ]
})
export class SoldierRegisterComponent {
  soldierForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private soldierService: SoldierService
  ) {
    this.soldierForm = this.fb.group({
      name: ['', Validators.required],
      surname: ['', Validators.required],
      phone_number: ['', [Validators.required, Validators.pattern(/^\+380\d{9}$/)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
      unit: [''],
      subsubunit: [''],
      battalion: ['']
    });
  }

  onSubmit(): void {
    if (this.soldierForm.valid) {
      this.soldierService.create(this.soldierForm.value).subscribe({
        next: () => {
          Swal.fire({
            icon: 'success',
            title: 'Успішна реєстрація!',
            text: 'Тепер ви можете увійти.',
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
            text: 'Спробуйте ще раз або перевірте дані.',
            confirmButtonColor: '#39736b',
            confirmButtonText: 'Гаразд',
            customClass: {
              confirmButton: 'montserrat-button'
            }
          });
        }
      });
    }
  }

  goToLogin(): void {
    this.router.navigate(['/login']);
  }
}
