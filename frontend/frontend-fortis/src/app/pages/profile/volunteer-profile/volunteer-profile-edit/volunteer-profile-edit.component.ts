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
import { RouterModule } from '@angular/router';


@Component({
  selector: 'app-volunteer-profile-edit',
  standalone: true,
  templateUrl: './volunteer-profile-edit.component.html',
  styleUrls: ['./volunteer-profile-edit.component.css'],
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
export class VolunteerProfileEditComponent {
  logout() {
    console.log('Вихід з акаунта');
  }

  showSearch = false;
  searchQuery = '';


  toggleSearch() {
    this.showSearch = !this.showSearch;
  }


}
