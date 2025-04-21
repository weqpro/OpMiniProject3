import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTabsModule } from '@angular/material/tabs';
import { MatIconModule } from '@angular/material/icon';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { FormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { MatChipsModule } from '@angular/material/chips';
import {Router, RouterModule} from '@angular/router';
import {SoldierService} from '../../../services/soldier.service';
import {VolonteerService} from '../../../services/volunteer.service';


@Component({
  selector: 'app-volunteer-profile',
  standalone: true,
  templateUrl: './volunteer-profile.component.html',
  styleUrls: ['./volunteer-profile.component.css'],
  imports: [
    MatChipsModule,
    CommonModule,
    MatTabsModule,
    MatIconModule,
    MatExpansionModule,
    MatFormFieldModule,
    MatInputModule,
    MatCheckboxModule,
    MatButtonModule,
    FormsModule,
    MatMenuModule,
    RouterModule,

  ]
})
export class VolunteerProfileComponent {


  // profileData = {
  //   name: 'Андрій',
  //   surname: 'Шевченко',
  //   email: 'andrii.shevchenko@army.ua',
  //   phone_number: '+380671234567',
  //   rating:4,
  //   review:'good',
  //   description:'oaoa'
  // };
  profileData: any = null;
  constructor(
    private router: Router,private volunteerService: VolonteerService
  ) {}


  ngOnInit(): void {
    this.volunteerService.getProfile().subscribe({
      next: data => this.profileData = data,
      error: err => {
        console.error('Не вдалося завантажити профіль волонтера:', err);
      }
    });
  }
  editProfile() {
    this.router.navigate(['app-volunteer-profile-edit']);
  }

  changePassword() {
    this.router.navigate(['app-volunteer-change-password']);
  }
  logout() {
    localStorage.removeItem('token');
    this.router.navigateByUrl('/login', { replaceUrl: true });
  }


  showSearch = false;
  searchQuery = '';


  toggleSearch() {
    this.showSearch = !this.showSearch;
}


}