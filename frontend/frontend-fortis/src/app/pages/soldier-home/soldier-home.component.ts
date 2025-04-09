import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';

@Component({
  selector: 'app-soldier-home',
  standalone: true,
  templateUrl: './soldier-home.component.html',
  styleUrls: ['./soldier-home.component.css'],
  imports: [
    RouterModule,
    MatFormFieldModule,
    MatInputModule,
    MatIconModule,
    MatButtonModule,
    MatMenuModule
  ]
})
export class SoldierHomeComponent {
  selectCategory(category: string) {
    console.log('Обрано категорію:', category);
  }

  logout(): void {
    console.log('Користувач вийшов');
  }

}
