import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {MyRequestsComponent} from './my-request-soldier/my-request-soldier.component';
@Component({
  selector: 'app-root',
  imports: [RouterOutlet, MyRequestsComponent, MyRequestsComponent],
  templateUrl: './app.component.html',
  standalone: true,
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend-fortis';
}


