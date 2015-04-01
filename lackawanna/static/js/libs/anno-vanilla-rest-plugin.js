/**
 * A basic plugin to store annotations on a REST-style HTTP/JSON endpoint.
 */

annotorious.plugin.VanillaREST = (function () {
    'use strict';
    function VanillaREST(options) {

        /** @private **/
        this._annotations = [];

        /** @private **/
        this._loadIndicators = [];


        this.options = {
            extraAnnotationData: {},
            loadFromSearch: false,
            prefix: '/store',
            urls: {
                create: '/annotation',
                read: '/annotations',
                update: '/annotation/:id',
                destroy: '/annotation/:id',
                search: '/annotations/search?query=*&limit=1000'
            }
        };

        this.options = jQuery.extend(this.options, options);
    };


    VanillaREST.prototype.initPlugin = function (anno) {
        var self = this;
        anno.addHandler('onAnnotationCreated', function (annotation) {
            self._create(annotation);
        });

        anno.addHandler('onAnnotationUpdated', function (annotation) {
            self._update(annotation);
        });

        anno.addHandler('onAnnotationRemoved', function (annotation) {
            self._delete(annotation);
        });

        self._loadAnnotations(anno);
    };

    VanillaREST.prototype.onInitAnnotator = function (annotator) {
        var spinner = this._newLoadIndicator();
        annotator.element.appendChild(spinner);
        this._loadIndicators.push(spinner);
    };


    /**
     * @private
     */
    VanillaREST.prototype._loadAnnotations = function (anno) {
        var self = this;
        var url = '';
        if (this.options.loadFromSearch === false) {
            url = this._getActionUrl('read', null);
        } else {
            url = this._getActionUrl('search', null);
        }
        jQuery.getJSON(url, function (data) {
            try {
                jQuery.each(data, function (index, data) {
                    var annotation = {};

                    if (typeof data['source'] != 'undefined' && typeof data['id'] != 'undefined') {
                        annotation = data['source'];
                        annotation.id = data['id'];
                    } else if (data !== null) {
                        annotation = data;
                    } else {
                        return;
                    }

                    // check for required properties
                    var reqProp = ['src','text','shapes','context'];
                    for (var rp in reqProp) {
                        if (reqProp.hasOwnProperty(rp) && !annotation.hasOwnProperty(reqProp[rp])) {
                            return;
                        }
                    }

                    if (jQuery.inArray(annotation.id, self._annotations) < 0) {
                        self._annotations.push(annotation.id);
                        if (!annotation.shape && annotation.shapes[0].geometry) {
                            anno.addAnnotation(annotation);
                        }
                    }
                });
            } catch (e) {
                self._showError(e);
            }

            // Remove all load indicators
            jQuery.each(self._loadIndicators, function (idx, spinner) {
                jQuery(spinner).remove();
            });
        }).fail(function(jqXHR) {
            self._onResponseError(jqXHR, 'load');
        });
    };


    /**
     * @private
     */
    VanillaREST.prototype._create = function (annotation) {
        var self = this;
        jQuery.post(this._getActionUrl('create', null), this._getAnnotationData(annotation), function (response) {
            annotation.id = response['id'];
        }).fail(function(jqXHR) {
            self._onResponseError(jqXHR, 'create');
        });
    };

    /**
     * @private
     */
    VanillaREST.prototype._update = function (annotation) {
        var self = this;
        jQuery.ajax({
            url: this._getActionUrl('update', annotation.id),
            type: 'PUT',
            data: this._getAnnotationData(annotation)
        }).fail(function(jqXHR) {
            self._onResponseError(jqXHR, 'update');
        });
    };

    /**
     * @private
     */
    VanillaREST.prototype._delete = function (annotation) {
        jQuery.ajax({
            url: this._getActionUrl('destroy', annotation.id),
            type: 'DELETE'
        }).fail(function(jqXHR) {
            self._onResponseError(jqXHR, 'delete');
        });
    };


    /**
     * @private
     */
    VanillaREST.prototype._newLoadIndicator = function () {
        var outerDIV = document.createElement('div');
        outerDIV.className = 'annotorious-rest-plugin-load-outer';

        var innerDIV = document.createElement('div');
        innerDIV.className = 'annotorious-rest-plugin-load-inner';

        outerDIV.appendChild(innerDIV);
        return outerDIV;
    };

    /**
     * Get url for given action
     * @private
     * @param {string} action
     * @param {int} id
     * @returns {string} returns url for given action
     */
    VanillaREST.prototype._getActionUrl = function (action, id) {
        var url;
        url = this.options.prefix !== null ? this.options.prefix : '';
        url += this.options.urls[action];
        url = url.replace(/\/:id/, id !== null ? '/' + id : '');
        url = url.replace(/:id/, id !== null ? id : '');
        return url;
    };

    VanillaREST.prototype._getAnnotationData = function (annotation) {
        var data;
        jQuery.extend(annotation, this.options.extraAnnotationData);
        data = JSON.stringify(annotation);
        return data;
    };

    VanillaREST.prototype._onResponseError = function(jqXHR, action) {
        var message = "Sorry we could not " + action + " this annotation";
        if (action === 'search') {
            message = "Sorry we could not search the store for annotations";
        } else if (action === 'read') {
            message = "Sorry we could not " + action + " the annotations from the store";
        }
        switch (jqXHR.status) {
            case 401:
                message = "Sorry you are not allowed to " + action + " this annotation";
                break;
            case 404:
                message = "Sorry we could not connect to the annotations store";
                break;
            case 500:
                message = "Sorry something went wrong with the annotation store";
        }
        this.showNotification(message, 'error');
        return console.error("API request failed: '" + jqXHR.status + "'");
    };


    VanillaREST.prototype.showNotification = function (message, type) {
        // TODO prettier notification message
        // TODO fire event onShowNotification so that translator plugin can take care of translating the message first.
        window.alert(message);
        console.log(message);
    };



    return VanillaREST;
}());
