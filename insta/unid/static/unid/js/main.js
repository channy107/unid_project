function heartChange1() {
							$(document).ready(function() {
								var dString = parseInt($('#dallor1').text());
								var hString = parseInt($('#heart1').text());

								hString = hString + parseInt(1);

								$('#heart1').text(hString);

								if (hString % 10 == 0)
									dString = dString + parseInt(1);

									$("#dallor1").text(dString);

							});

						};