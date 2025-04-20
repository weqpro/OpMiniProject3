import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { SoldierService } from '../../../services/soldier.service'


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
      surname: ['', Validators.required],
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      phone_number: ['', Validators.required],
      unit: ['', Validators.required],
      subsubunit: ['', Validators.required],
      battalion: ['', Validators.required],
    });
  }

  onSubmit() {
    if (this.soldierForm.valid) {
      console.log(this.soldierForm.value);
      this.soldierService.create(this.soldierForm.value).subscribe({
        next: () => {
          this.router.navigate(['/requests-filter']);
        },
        error: (err: any) => {
          console.error(err);
          alert('Помилка реєстрації');
  
        }
      });
    }
  }

  goToLogin() {
    this.router.navigate(['/login']);
  }
}
