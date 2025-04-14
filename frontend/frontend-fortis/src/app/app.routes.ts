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
import { CatalogComponent } from './pages/catalog/catalog/catalog.component';
import { VolunteerHomeComponent } from './pages/volunteer-home/volunteer-home.component';
export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'soldier-home', component: SoldierHomeComponent },
  { path: 'create', component: CreatePostComponent },
  { path: 'profile/soldier', component: SoldierProfileComponent },
  { path: 'profile/volunteer', component: VolunteerProfileComponent },
  { path: 'login', component: LoginComponent },
  { path: 'role-selection', component: RoleSelectionComponent },
  { path: 'register', component: RoleSelectionComponent },
  { path: 'profile/soldier', component: SoldierProfileComponent },
  { path: 'volunteer-home', component: VolunteerHomeComponent },
  // { path: 'own-requests-soldier', component: OwnRequestSoldierComponent }
  { path: 'register/soldier', component: SoldierRegisterComponent },
  { path: 'register/volunteer', component: VolunteerRegisterComponent },
  { path: 'catalog', component: CatalogComponent},
];
