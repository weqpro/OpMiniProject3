import { Routes } from '@angular/router';
import { SoldierHomeComponent } from './pages/soldier-home/soldier-home.component';
import { CreatePostComponent } from './pages/create-post/create-post.component';
import { SoldierProfileComponent } from './pages/profile/soldier-profile/soldier-profile.component';
import { LoginComponent } from './pages/login/login.component';
import { RoleSelectionComponent } from './pages/role-selection/role-selection.component';

export const routes: Routes = [
  { path: '', component: SoldierHomeComponent },
  { path: 'create', component: CreatePostComponent },
  { path: 'profile/soldier', component: SoldierProfileComponent},
  { path: 'login', component: LoginComponent },
  { path: 'role-selection', component: RoleSelectionComponent },
  { path: 'register', component: RoleSelectionComponent }
  // { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGuard] },
];
