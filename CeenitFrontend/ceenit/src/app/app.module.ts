import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table';
import {MatGridListModule} from '@angular/material/grid-list';

import { AppComponent } from './app.component';
import { CeenitListsComponent } from './ceenit-lists/ceenit-lists.component';
import { CeenitReviewsComponent } from './ceenit-reviews/ceenit-reviews.component';
import { CeenitWatchlistComponent } from './ceenit-watchlist/ceenit-watchlist.component';
import { CeenitTimelineComponent } from './ceenit-timeline/ceenit-timeline.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RoutingModule } from './routing/routing.module';
import { HomeComponent } from './home/home.component';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { SearchComponent } from './search/search.component';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MovieListComponent } from './pages/movie-list/movie-list.component';
import { HttpClientModule } from '@angular/common/http';
import { MoviePictureListComponent } from './movie-picture-list/movie-picture-list.component';
import { MovieDetailComponent } from './movie-detail/movie-detail.component';
import { CeenitListsContentComponent } from './ceenit-lists-content/ceenit-lists-content.component'

@NgModule({
  declarations: [
    AppComponent,
    CeenitListsComponent,
    CeenitReviewsComponent,
    CeenitWatchlistComponent,
    CeenitTimelineComponent,
    HomeComponent,
    SearchComponent,
    MovieListComponent,
    MoviePictureListComponent,
    MovieDetailComponent,
    CeenitListsContentComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatListModule,
    MatToolbarModule,
    MatGridListModule,
    MatIconModule,
    MatButtonModule,
    RoutingModule,
    MatFormFieldModule,
    MatInputModule,
    HttpClientModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
