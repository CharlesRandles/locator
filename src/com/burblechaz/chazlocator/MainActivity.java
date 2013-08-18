package com.burblechaz.chazlocator;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;

import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.text.format.Time;
import android.view.Menu;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends Activity {

	public final static String EXTRA_MESSAGE="com.burblechaz.chazlocator.MESSAGE";
	
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
        
    public void showLocation(View view) {
  	    		
    		//This needs refactoring

    
    		//Get location	
    		LocationManager locationManager = 
    				(LocationManager) this.getSystemService(Context.LOCATION_SERVICE);
    		LocationListener locationListener = new LocationListener() {
    			public void onLocationChanged(Location location) {
    	    			Time now = new Time();
    	    			now.setToNow();
    	    			String currentTime = now.format("%H:%M:%S %e-%m-%G");
    	    			TextView status = (TextView) findViewById(R.id.location_status);
    	    			String status_string = currentTime;
    	    			double latitude = location.getLatitude();
    	    			double longitude = location.getLongitude();
    	    			double altitude = location.getAltitude();
    	    			status_string = status_string + String.format("\nLat:%1.3f", latitude);
    	    			status_string = status_string + String.format("\nLon:%1.3f", longitude);
    	    			status_string = status_string + String.format("\nAlt:%1.3f", altitude);
    	    			status.setText(status_string);
    	    			
    	    			publishLocation(latitude, longitude, altitude, currentTime);
    	    			
    			}

    			@Override
    			public void onProviderDisabled(String arg0) {
    				// TODO Auto-generated method stub
    				
			}
    			
			@Override
			public void onProviderEnabled(String arg0) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void onStatusChanged(String arg0, int arg1, Bundle arg2) {
				// TODO Auto-generated method stub
					
			}
    		};
    		//Go and find us 
    		locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 1000 * 60 *5 , 0, locationListener);
    		
    }

    /*
     * Do an HTTP Post of the data
     */
	protected void publishLocation(double latitude, double longitude,double altitude, String currentTime) {

		String s_lat = String.format("%1.3f", latitude);
		String s_long = String.format("%1.3f", longitude);
		String s_alt = String.format("%1.3f", altitude);
		new PublishTask().execute(s_lat, s_long, s_alt, currentTime);
		
	}
}
