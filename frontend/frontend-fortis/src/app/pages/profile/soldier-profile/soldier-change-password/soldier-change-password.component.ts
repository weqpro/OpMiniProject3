import { Component } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router} from '@angular/router';
import {SoldierService} from '../../../../services/soldier.service';

@Component({
  selector: 'app-soldier-change-password',
  imports: [],
  templateUrl: './soldier-change-password.component.html',
  standalone: true,
  styleUrl: './soldier-change-password.component.css'
})
export class SoldierChangePasswordComponent {
  form: FormGroup;

  constructor(private fb: FormBuilder, private soldierService: SoldierService, private router: Router) {
    this.form = this.fb.group({
      current_password: ['', Validators.required],
      new_password: ['', Validators.required],
      new_password_repeat: ['', Validators.required]
    });
  }

  submit() {
    const { current_password, new_password, new_password_repeat } = this.form.value;

    if (new_password !== new_password_repeat) {
      alert('Паролі не збігаються');
      return;
    }

    this.soldierService.changePassword({ current_password, new_password }).subscribe({
      next: () => {
        alert('Пароль змінено');
        this.router.navigate(['/profile/soldier']);
      },
      error: err => alert('Помилка зміни пароля')
    });
  }
}

