import { Routes } from '@angular/router';
import { SoldierHomeComponent } from './pages/soldier-home/soldier-home.component';
import { CreatePostComponent } from './pages/create-post/create-post.component';
import { SoldierProfileComponent } from './pages/profile/soldier-profile/soldier-profile.component';

export const routes: Routes = [
  { path: '', component: SoldierHomeComponent },
  { path: 'create', component: CreatePostComponent },
  { path: 'profile/soldier', component: SoldierProfileComponent }
];