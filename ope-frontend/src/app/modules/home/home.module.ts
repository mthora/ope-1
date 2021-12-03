import { ComponentsModule } from './../../components/components.module';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { HomeScreenComponent } from './home-screen/home-screen.component';
import { MatSidenavModule } from '@angular/material/sidenav';
import { LoginScreenComponent } from './login-screen/login-screen.component';
import { MyOrdersComponent } from './my-orders/my-orders.component';


@NgModule({
  declarations: [
    HomeScreenComponent,
    LoginScreenComponent,
    MyOrdersComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    MatSidenavModule
  ],
  exports: [
    HomeScreenComponent,
    LoginScreenComponent,
    MyOrdersComponent
  ]
})
export class HomeModule { }
