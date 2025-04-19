import { Routes } from '@angular/router';
import { SoldierHomeComponent } from './pages/soldier-home/soldier-home.component';
import { CreatePostComponent } from './pages/create-post/create-post.component';
import { SoldierProfileComponent } from './pages/profile/soldier-profile/soldier-profile.component';
import { VolunteerProfileComponent } from './pages/profile/volunteer-profile/volunteer-profile.component';
import { LoginComponent } from './pages/login/login.component';
import { HomeComponent } from './pages/home-page/home-page.component';
import { RoleSelectionComponent } from './pages/role-selection/role-selection.component';
import { VolunteerRegisterComponent } from './pages/register/volunteer-register/volunteer-register.component';
import { SoldierRegisterComponent } from './pages/register/soldier-register/soldier-register.component';
import { RequestsFilterComponent } from './pages/requests-filter/requests-filter.component';
import { MyRequestsComponent } from './pages/my-request-soldier/my-request-soldier.component'
import { ReviewComponent } from './pages/review/review.component'
export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'soldier-home', component: SoldierHomeComponent },
  { path: 'create', component: CreatePostComponent },
  { path: 'profile/soldier', component: SoldierProfileComponent },
  { path: 'profile/volunteer', component: VolunteerProfileComponent },
  { path: 'login', component: LoginComponent },
  { path: 'role-selection', component: RoleSelectionComponent },
  { path: 'register', component: RoleSelectionComponent },
  { path: 'requests-filter', component: RequestsFilterComponent },
  { path: 'my-requests-soldier', component: MyRequestsComponent },
  { path: 'register/soldier', component: SoldierRegisterComponent },
  { path: 'register/volunteer', component: VolunteerRegisterComponent },
  {path: 'review', component: ReviewComponent },
];
