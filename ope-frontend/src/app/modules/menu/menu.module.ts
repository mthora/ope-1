import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SubMenuScreenComponent } from './sub-menu-screen/sub-menu-screen.component';
import { ComponentsModule } from 'src/app/components/components.module';
import { MatSidenavModule } from '@angular/material/sidenav';
import { PlatesComponent } from 'src/app/components/plates/plates.component';
import { PlatesScreenComponent } from './plates-screen/plates-screen.component';
import { LanchesScreenComponent } from './lanches-screen/lanches-screen.component';
import { Bebidas_SobremesasScreenComponent } from './bebidas_sobremesas-screen/bebidas_sobremesas-screen.component';



@NgModule({
  declarations: [
    SubMenuScreenComponent,
    PlatesScreenComponent,
    LanchesScreenComponent,
    Bebidas_SobremesasScreenComponent
    
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    MatSidenavModule
  ]
})
export class MenuModule { }
