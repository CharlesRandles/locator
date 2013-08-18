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

import android.widget.TextView;
import android.os.AsyncTask;

public class PublishTask extends AsyncTask<String, String, String> {
	@Override
	protected String doInBackground(String... data) {
		
		String latitude = data[0];
		String longitude = data[1];
		String altitude = data[2];
		String currentTime = data[3];

		List<NameValuePair> params = new ArrayList<NameValuePair>(4);
		params.add(new BasicNameValuePair("latitude", latitude));
		params.add(new BasicNameValuePair("longitude", longitude));
		params.add(new BasicNameValuePair("altitude", altitude));
		params.add(new BasicNameValuePair("time", currentTime));
		
		HttpClient httpClient= new DefaultHttpClient();
		HttpPost httpPost = new HttpPost("http://burblechaz.com/chaz_locator/update_location.py");
		
		try {
			httpPost.setEntity(new UrlEncodedFormEntity(params));
			HttpResponse response = httpClient.execute(httpPost);
			int code= response.getStatusLine().getStatusCode();
			if (code == 200){
				return "Status published";
			}
		}
		catch (ClientProtocolException ex){
			return ex.toString();
		}
		catch (IOException ex) {
			return ex.toString();
		}
		catch (Exception ex){
			return ex.toString();
		}

		// TODO Auto-generated method stub
		return null;
	}
	
	protected void onPostExecute(String status) {
		
	}

}
