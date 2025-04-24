import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { RouterLink } from '@angular/router';
import { SoldierService } from '../../../../services/soldier.service';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';

@Component({
  selector: 'app-soldier-change-password',
  templateUrl: './soldier-change-password.component.html',
  styleUrls: ['./soldier-change-password.component.css'],
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    RouterLink,
    MatFormFieldModule,
    MatInputModule,
    MatIconModule,
    MatMenuModule,
    MatButtonModule,
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
      alert('Усі поля обов’язкові!');
      return;
    }

    if (new_password !== new_password_repeat) {
      alert('Нові паролі не збігаються!');
      return;
    }

    if (new_password === current_password) {
      alert('Новий пароль не може бути таким самим, як старий!');
      return;
    }

    this.soldierService.changePassword({
      current_password,
      new_password
    }).subscribe({
      next: () => {
        alert('Пароль успішно змінено!');
        this.router.navigate(['/profile/soldier']);
      },
      error: err => {
        console.error('Помилка зміни пароля:', err);
        alert('Не вдалося змінити пароль.');
      }
    });
  }
}