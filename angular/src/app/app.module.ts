import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LandingPageComponent } from './pages/landing-page/landing-page.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { HeaderComponent } from './shared/components/layout/header/header.component';
import { MainCoverComponent } from './shared/components/layout/main-cover/main-cover.component';
import { MainQuoteComponent } from './shared/components/layout/main-quote/main-quote.component';
import { FeaturesSectionComponent } from './shared/components/layout/features-section/features-section.component';
import { FeatureComponent } from './shared/components/layout/feature/feature.component';
import { SmartphoneRenderComponent } from './shared/components/layout/smartphone-render/smartphone-render.component';
import { BasicSectionComponent } from './shared/components/layout/basic-section/basic-section.component';
import { AltSectionComponent } from './shared/components/layout/alt-section/alt-section.component';
import { FooterComponent } from './shared/components/layout/footer/footer.component';
import { LoginComponent } from './shared/components/login/login.component';
import { DashboardElementComponent } from './shared/components/dashboard-element/dashboard-element.component';
import { NgxRoslibService } from 'ngx-roslib';

@NgModule({
  declarations: [
    AppComponent,
    LandingPageComponent,
    DashboardComponent,
    HeaderComponent,
    MainCoverComponent,
    MainQuoteComponent,
    FeaturesSectionComponent,
    FeatureComponent,
    SmartphoneRenderComponent,
    BasicSectionComponent,
    AltSectionComponent,
    FooterComponent,
    LoginComponent,
    DashboardElementComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [NgxRoslibService],
  bootstrap: [AppComponent]
})
export class AppModule { }
