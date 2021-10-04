import { SubMenuScreenComponent } from './modules/menu/sub-menu-screen/sub-menu-screen.component';
import { LoginScreenComponent } from './modules/home/login-screen/login-screen.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeScreenComponent } from './modules/home/home-screen/home-screen.component';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { PlatesScreenComponent } from './modules/menu/plates-screen/plates-screen.component';
import { LanchesScreenComponent } from './modules/menu/lanches-screen/lanches-screen.component';
import { Bebidas_SobremesasScreenComponent } from './modules/menu/bebidas_sobremesas-screen/bebidas_sobremesas-screen.component';

const routes: Routes = [
  {path: '', component: HomeScreenComponent },
  {path: 'acesso', component: LoginScreenComponent},
  {path: 'cardapio', children: [
    {path: '', component: SubMenuScreenComponent},
    {path: 'pratos', component: PlatesScreenComponent},
    {path: 'lanches', component: LanchesScreenComponent},
    {path: 'bebidas_sobremesas', component: Bebidas_SobremesasScreenComponent}
  ]},


  {path: '404', component: NotFoundComponent},
  {path: '**', redirectTo: '/404'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
