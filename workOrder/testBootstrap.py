<div class="container">
    <div class="row">
        <div class="col-md-8">
            <form action="https://formspree.io/{{page.email}}" method="POST" role="form">
                {% if form.subject.errors %}
                <ol role="alertdialog">
                    {% for error in form.subject.errors %}
                    <li role="alert"><strong>{{ error|escape }}</strong></li>
                    {% endfor %}
                </ol>
                {% endif %}
		
                {% for field in form %}
                <div class="fieldWrapper form-group" aria-required={% if field.field.required %}"true"{% else %}"false"{% endif %}>
                    {{ field.label_tag }}{% if field.field.required %}<span class="required">*</span>{% endif %}
                    {{ field }}
                    {% if field.help_text %}
                    <p class="help">{{ field.help_text|safe }}</p>
                    {% endif %}
                </div>
                {% endfor %}
		<input type="submit" class="btn btn-primary mb-2" value="Submit" />
            </form>
        </div>
	<div class="col-md-4">
	    <!-- Other column -->
	</div>
    </div>
</div>
