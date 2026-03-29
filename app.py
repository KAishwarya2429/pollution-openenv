import gradio as gr

def pollution_report(location, aqi):
    try:
        aqi = int(aqi)
    except:
        return "❌ Please enter a valid AQI number"

    if aqi <= 50:
        status = "🟢 Good"
        message = "Air quality is good. Enjoy outdoor activities!"
    elif aqi <= 100:
        status = "🟡 Moderate"
        message = "Air quality is acceptable. Sensitive people should be careful."
    elif aqi <= 200:
        status = "🟠 Poor"
        message = "Air quality is poor. Avoid outdoor activities."
    else:
        status = "🔴 Very Poor"
        message = "Air quality is very unhealthy. Stay indoors!"

    return f"📍 Location: {location}\n🌫 AQI: {aqi}\nStatus: {status}\n\n{message}"


demo = gr.Interface(
    fn=pollution_report,
    inputs=[
        gr.Textbox(label="Enter Location"),
        gr.Textbox(label="Enter AQI (Air Quality Index)")
    ],
    outputs="text",
    title="🌍 Pollution Awareness App",
    description="Check air quality status and get safety advice based on AQI."
)

demo.launch()