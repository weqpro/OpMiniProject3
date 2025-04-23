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
  showSearch = false;
  searchQuery = '';
  originalData: any = {};

  constructor(
    private fb: FormBuilder,
    private soldierService: SoldierService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.profileForm = this.fb.group({
      name: [''],
      surname: [''],
      phone_number: [''],
      unit: [''],
      subsubunit: [''],
      battalion: [''],
      password: ['', Validators.required]  // current password for confirmation
    });

    this.loadProfile();
  }
  profileData: any = null;
  // profileData = {
  //   name: 'Андрій',
  //   surname: 'Шевченко',
  //   email: 'andrii.shevchenko@army.ua',
  //   phone_number: '+380671234567',
  //   unit: '80-та окрема десантно-штурмова бригада',
  //   subsubunit: '2-й взвод',
  //   battalion: '3-й батальйон',
  //   description:'oaoa'
  // };

  loadProfile() {
    this.soldierService.getProfile().subscribe({
      next: (data) => {
        this.profileData = data;
      },
      error: (err) => {
        console.error('Помилка завантаження профілю:', err);
      }
    });
  }

  // loadProfile() {
  //   this.soldierService.getProfile().subscribe({
  //     next: (data) => {
  //       this.originalData = data;
  //       this.profileForm.patchValue({
  //         name: data.name,
  //         surname: data.surname,
  //         phone_number: data.phone_number,
  //         unit: data.unit,
  //         subsubunit: data.subsubunit,
  //         battalion: data.battalion
  //       });
  //     },
  //     error: (err) => {
  //       console.error('Помилка завантаження профілю:', err);
  //     }
  //   });
  // }

  onSubmit() {

    const formData = this.profileForm.value;

    this.soldierService.updateProfile(formData).subscribe({
      next: () => {
        alert('Профіль оновлено');
        this.router.navigate(['/profile/soldier']);
      },
      error: (err) => {
        console.error('Помилка оновлення:', err);
        alert('Неправильний пароль або інша помилка');
      }
    });
  }

  toggleSearch() {
    this.showSearch = !this.showSearch;
  }

  cancel(){
    this.router.navigate(['profile/soldier']);
  }
}
