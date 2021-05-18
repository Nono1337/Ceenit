import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';

import { AppComponent } from './app.component';
import { CeenitListsComponent } from './ceenit-lists/ceenit-lists.component';
import { CeenitReviewsComponent } from './ceenit-reviews/ceenit-reviews.component';
import { CeenitWatchlistComponent } from './ceenit-watchlist/ceenit-watchlist.component';
import { CeenitTimelineComponent } from './ceenit-timeline/ceenit-timeline.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RoutingModule } from './routing/routing.module';
import { HomeComponent } from './home/home.component';

import { SearchComponent } from './search/search.component'

@NgModule({
  declarations: [
    AppComponent,
    CeenitListsComponent,
    CeenitReviewsComponent,
    CeenitWatchlistComponent,
    CeenitTimelineComponent,
    HomeComponent,
    SearchComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatListModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    RoutingModule,
    MatInputModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
