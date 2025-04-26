import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { VolonteerService } from '../../../../services/volunteer.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { RouterLink } from '@angular/router';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-volunteer-change-password',
  templateUrl: './volunteer-change-password.component.html',
  styleUrls: ['./volunteer-change-password.component.css'],
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    RouterLink,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatMenuModule,
    MatIconModule
  ]
})
export class VolunteerChangePasswordComponent {
  passwordData = {
    current_password: '',
    new_password: '',
    new_password_repeat: ''
  };

  constructor(private volunteerService: VolonteerService, private router: Router) {}

  submit(): void {
    const { current_password, new_password, new_password_repeat } = this.passwordData;

    if (!current_password || !new_password || !new_password_repeat) {
      Swal.fire({
        icon: 'warning',
        title: 'Увага',
        text: 'Усі поля обов’язкові!',
        confirmButtonColor: '#39736b',
        confirmButtonText: 'Окей'
      });
      return;
    }

    if (new_password !== new_password_repeat) {
      Swal.fire({
        icon: 'warning',
        title: 'Увага',
        text: 'Нові паролі не збігаються!',
        confirmButtonColor: '#39736b',
        confirmButtonText: 'Окей'
      });
      return;
    }

    if (new_password === current_password) {
      Swal.fire({
        icon: 'warning',
        title: 'Увага',
        text: 'Новий пароль не може бути таким самим, як старий!',
        confirmButtonColor: '#39736b',
        confirmButtonText: 'Окей'
      });
      return;
    }

    this.volunteerService.changePassword({
      current_password,
      new_password
    }).subscribe({
      next: () => {
        Swal.fire({
          icon: 'success',
          title: 'Успішно!',
          text: 'Пароль змінено!',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Окей'
        }).then(() => {
          this.router.navigate(['/profile/volunteer']);
        });
      },
      error: err => {
        console.error('Помилка зміни пароля:', err);
        Swal.fire({
          icon: 'error',
          title: 'Помилка',
          text: 'Не вдалося змінити пароль.',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Окей'
        });
      }
    });
  }
}
