import { Routes } from '@angular/router';
import { CreatePostComponent } from './pages/create-post/create-post.component';
import { SoldierProfileComponent } from './pages/profile/soldier-profile/soldier-profile.component';
import { VolunteerProfileComponent } from './pages/profile/volunteer-profile/volunteer-profile.component';
import { LoginComponent } from './pages/login/login.component';
import { HomeComponent } from './pages/home-page/home-page.component';
import { RoleSelectionComponent } from './pages/role-selection/role-selection.component';
import { VolunteerRegisterComponent } from './pages/register/volunteer-register/volunteer-register.component';
import { SoldierRegisterComponent } from './pages/register/soldier-register/soldier-register.component';
import { RequestsFilterComponent } from './pages/requests-filter/requests-filter.component';
import { ReviewComponent } from './pages/review/review.component'
import {
  SoldierChangePasswordComponent
} from './pages/profile/soldier-profile/soldier-change-password/soldier-change-password.component';
import {
  SoldierProfileEditComponent
} from './pages/profile/soldier-profile/soldier-profile-edit/soldier-profile-edit.component';
import {
  VolunteerChangePasswordComponent
} from './pages/profile/volunteer-profile/volunteer-change-password/volunteer-change-password.component';
import {
  VolunteerProfileEditComponent
} from './pages/profile/volunteer-profile/volunteer-profile-edit/volunteer-profile-edit.component';
import { EditRequestComponent } from './pages/edit-request/edit-request.component';
import { AuthGuard } from './guards/auth.guard';
export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'create', component: CreatePostComponent,  canActivate: [AuthGuard]},
  { path: 'profile/soldier', component: SoldierProfileComponent,  canActivate: [AuthGuard] },
  { path: 'profile/volunteer', component: VolunteerProfileComponent,  canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent },
  { path: 'role-selection', component: RoleSelectionComponent },
  { path: 'register', component: RoleSelectionComponent },
  { path: 'requests-filter', component: RequestsFilterComponent,  canActivate: [AuthGuard] },
  { path: 'register/soldier', component: SoldierRegisterComponent },
  { path: 'register/volunteer', component: VolunteerRegisterComponent },
  { path: 'review/:id', component: ReviewComponent,  canActivate: [AuthGuard] },
  { path: 'app-soldier-change-password', component: SoldierChangePasswordComponent,  canActivate: [AuthGuard] },
  { path: 'app-soldier-profile-edit', component: SoldierProfileEditComponent,  canActivate: [AuthGuard]},
  { path: 'app-volunteer-change-password', component: VolunteerChangePasswordComponent,  canActivate: [AuthGuard]},
  { path: 'app-volunteer-profile-edit', component: VolunteerProfileEditComponent,  canActivate: [AuthGuard]},
  { path: 'edit-request/:id', component: EditRequestComponent,  canActivate: [AuthGuard] }
];