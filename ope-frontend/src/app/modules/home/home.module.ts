import { ComponentsModule } from './../../components/components.module';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { HomeScreenComponent } from './home-screen/home-screen.component';
import { MatSidenavModule } from '@angular/material/sidenav';
import { LoginScreenComponent } from './login-screen/login-screen.component';


@NgModule({
  declarations: [
    HomeScreenComponent,
    LoginScreenComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    MatSidenavModule
  ],
  exports: [
    HomeScreenComponent,
    LoginScreenComponent
  ]
})
export class HomeModule { }
