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
      fullName: ['', Validators.required],
      phone: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onSubmit() {
    if (this.volunteerForm.valid) {
      console.log(this.volunteerForm.value);
      this.volunteerService.create(this.volunteerForm.value).subscribe({
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
