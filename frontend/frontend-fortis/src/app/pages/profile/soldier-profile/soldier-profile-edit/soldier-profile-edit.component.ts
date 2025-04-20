import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators} from '@angular/forms';
import {Router, RouterLink} from '@angular/router';
import {MatFormField, MatInput} from '@angular/material/input';
import {MatButton} from '@angular/material/button';
import {MatFormFieldModule} from '@angular/material/form-field';
import {SoldierService} from '../../../../services/soldier.service';

@Component({
  selector: 'app-soldier-profile-edit',
  templateUrl: './soldier-profile-edit.component.html',
  styleUrls: ['./soldier-profile-edit.component.css'],
  standalone: true,
  imports: [
    MatFormField,
    MatButton,
    RouterLink,
    FormsModule,
    MatInput,
    ReactiveFormsModule,
    MatFormFieldModule
  ]
})
export class SoldierProfileEditComponent implements OnInit {
  profileData: any = {
    name: 'Олександр',
    surname: 'Шевченко',
    phone_number: '+380671234567',
    email: 'oleksandr.shevchenko@army.ua',
    unit: '80-та окрема десантно-штурмова бригада',
    subsubunit: '2-й взвод',
    battalion: '3-й батальйон'
  };

  constructor(
    private soldierService: SoldierService,
    private router: Router
  ) {}


  form!: FormGroup;
  loading = true;
  ngOnInit(): void {
    this.soldierService.getProfile().subscribe({
      next: (data) => {
        this.profileData = data;
      },
      error: (err) => {
        console.error('Помилка завантаження профілю:', err);
      }
    });

    this.soldierService.getProfile().subscribe({
      next: data => {
        this.form.patchValue(data);
        this.loading = false;
      },
      error: err => {
        console.error('Не вдалося завантажити профіль:', err);
        this.loading = false;
      }
    });
  }

  submit(): void {
    if (this.form.valid) {
      this.soldierService.updateProfile(this.form.value).subscribe({
        next: () => {
          alert('Профіль оновлено!');
          this.router.navigate(['/profile/soldier']);
        },
        error: err => {
          console.error('Помилка оновлення профілю:', err);
          alert('Не вдалося оновити профіль.');
        }
      });
    }
  }
}
