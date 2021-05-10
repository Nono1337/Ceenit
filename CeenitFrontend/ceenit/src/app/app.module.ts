import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatSidenavModule } from '@angular/material/sidenav';

import { AppComponent } from './app.component';
import { CeenitListsComponent } from './ceenit-lists/ceenit-lists.component';
import { CeenitReviewsComponent } from './ceenit-reviews/ceenit-reviews.component';
import { CeenitWatchlistComponent } from './ceenit-watchlist/ceenit-watchlist.component';
import { CeenitTimelineComponent } from './ceenit-timeline/ceenit-timeline.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    CeenitListsComponent,
    CeenitReviewsComponent,
    CeenitWatchlistComponent,
    CeenitTimelineComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatSidenavModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
