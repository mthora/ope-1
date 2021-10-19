import { MatButtonModule } from '@angular/material/button';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SubMenuScreenComponent } from './sub-menu-screen/sub-menu-screen.component';
import { ComponentsModule } from 'src/app/components/components.module';
import { MatSidenavModule } from '@angular/material/sidenav';
import { PlatesScreenComponent } from './plates-screen/plates-screen.component';
import { LanchesScreenComponent } from './lanches-screen/lanches-screen.component';
import { Bebidas_SobremesasScreenComponent } from './bebidas_sobremesas-screen/bebidas_sobremesas-screen.component';
import { PromocoesScreenComponent } from './promocoes-screen/promocoes-screen.component';


@NgModule({
  declarations: [
    SubMenuScreenComponent,
    PlatesScreenComponent,
    LanchesScreenComponent,
    Bebidas_SobremesasScreenComponent,
    PromocoesScreenComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    MatSidenavModule,
    MatButtonModule
  ]
})
export class MenuModule { }
