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
  logout() {
    console.log('Вихід з акаунта');
}

  showSearch = false;
  searchQuery = '';


  toggleSearch() {
    this.showSearch = !this.showSearch;
}  
}
