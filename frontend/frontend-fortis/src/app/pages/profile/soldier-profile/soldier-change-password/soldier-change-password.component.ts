import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { SoldierService } from '../../../../services/soldier.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { RouterLink } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-soldier-change-password',
  templateUrl: './soldier-change-password.component.html',
  styleUrls: ['./soldier-change-password.component.css'],
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatIconModule,
    MatMenuModule,
    RouterLink,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule
  ]
})
export class SoldierChangePasswordComponent {
  passwordData = {
    current_password: '',
    new_password: '',
    new_password_repeat: ''
  };

  constructor(private soldierService: SoldierService, private router: Router) {}

  submit(): void {
    const { current_password, new_password, new_password_repeat } = this.passwordData;

    if (!current_password || !new_password || !new_password_repeat) {
      Swal.fire({
        icon: 'warning',
        title: 'Помилка',
        text: 'Усі поля обов’язкові!',
        confirmButtonColor: '#39736b',
        confirmButtonText: 'Окей'
      });
      return;
    }

    if (new_password.length < 8) {
      Swal.fire({
        icon: 'warning',
        title: 'Помилка',
        text: 'Пароль має бути не менше 8 символів!',
        confirmButtonColor: '#39736b',
        confirmButtonText: 'Окей'
      });
      return;
    }

    if (new_password !== new_password_repeat) {
      Swal.fire({
        icon: 'warning',
        title: 'Помилка',
        text: 'Нові паролі не збігаються!',
        confirmButtonColor: '#39736b',
        confirmButtonText: 'Окей'
      });
      return;
    }

    if (new_password === current_password) {
      Swal.fire({
        icon: 'warning',
        title: 'Помилка',
        text: 'Новий пароль не може бути таким самим, як старий!',
        confirmButtonColor: '#39736b',
        confirmButtonText: 'Окей'
      });
      return;
    }

    this.soldierService.changePassword({ current_password, new_password }).subscribe({
      next: () => {
        Swal.fire({
          icon: 'success',
          title: 'Успіх!',
          text: 'Пароль змінено успішно!',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Окей'
        }).then(() => {
          this.router.navigate(['/profile/soldier']);
        });
      },
      error: err => {
        console.error('Помилка зміни паролю:', err);
        Swal.fire({
          icon: 'error',
          title: 'Помилка',
          text: 'Не вдалося змінити пароль. Спробуйте ще раз.',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Окей'
        });
      }
    });
  }
}
