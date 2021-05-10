import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { CeenitListsComponent } from './ceenit-lists/ceenit-lists.component';
import { CeenitReviewsComponent } from './ceenit-reviews/ceenit-reviews.component';
import { CeenitWatchlistComponent } from './ceenit-watchlist/ceenit-watchlist.component';
import { CeenitTimelineComponent } from './ceenit-timeline/ceenit-timeline.component';

@NgModule({
  declarations: [
    AppComponent,
    CeenitListsComponent,
    CeenitReviewsComponent,
    CeenitWatchlistComponent,
    CeenitTimelineComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
