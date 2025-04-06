import { Component } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatSelectModule } from '@angular/material/select';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatChipsModule } from '@angular/material/chips';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatMenuModule } from '@angular/material/menu';

@Component({
  selector: 'app-create-post',
  standalone: true,
  templateUrl: './create-post.component.html',
  styleUrls: ['./create-post.component.css'],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule,
    MatFormFieldModule,
    MatInputModule,
    MatIconModule,
    MatButtonModule,
    MatSelectModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatChipsModule,
    MatAutocompleteModule,
    MatMenuModule
  ]
})
export class CreatePostComponent {
  allTags = [
    { name: 'Медицина', selected: false },
    { name: 'Спорядження', selected: false },
    { name: 'Продукти харчування', selected: false },
    { name: 'Транспорт', selected: false },
    { name: 'Звʼязок', selected: false },
    { name: 'Техніка', selected: false },
    { name: 'Одяг', selected: false }
  ];
  showSearch = false;
  searchQuery = '';

  toggleSearch() {
    this.showSearch = !this.showSearch;
  }
  constructor(private router: Router) {}

  selectCategory(category: string): void {
    console.log('Обрана категорія:', category);
  }

  logout(): void {
    console.log('Користувач вийшов');
  }
}