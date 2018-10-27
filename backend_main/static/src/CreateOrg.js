import React, { Component } from 'react';
import PropTypes from 'prop-types';
import TextField from "@material-ui/core/TextField/TextField";
import { withStyles } from "@material-ui/core";
import Onboarding from "./components/Onboarding";
import routes from './routes';
import connect from "react-redux/es/connect/connect";
import { SET_ORG_EMAIL, SET_ORG_NAME, SET_PASSWORD } from "./redux/user";
import Typography from "@material-ui/core/Typography/Typography";

class CreateOrg extends Component {
	state = { name: "", email: "", password: "", confirmPassword: "", error: "" };

	constructor(props) {
		super(props);
		//see templates/main.html
		document.addEventListener("animationstart", this.showDjangoError.bind(this), false);
	}
	showDjangoError() {
		if (event.animationName !== 'nodeInserted')
			return;
		const errorList = document.getElementsByClassName("errorlist")[0];
		if (errorList === undefined)
			return;
		const error = errorList.getElementsByTagName("li")[0];
		if (error === undefined)
			return;
		this.setState({error: error.textContent});
	}
	confirmPasswordError() {
		return this.state.password !== this.state.confirmPassword;
	}
	canContinue() {
		return this.state.name !== undefined && this.state.name !== "" &&
			this.state.email !== undefined && this.state.email !== "" &&
			this.state.password !== undefined && this.state.password !== "" &&
			!this.confirmPasswordError();
	}
	onClick() {
		this.props.setName(this.state.name);
		document.getElementById("id_username").value = this.state.email;
		document.getElementById("id_password1").value = this.state.password;
		document.getElementById("id_password2").value = this.state.confirmPassword;
		const form = document.getElementsByTagName("form")[0];
		form.submit();
	}
	render() {
		const { classes } = this.props;
		return (
			<Onboarding
				title={"Create an Organization Account"}
				button={"Continue"}
				link={routes.verifyCornellStatus.route}
				canClick={this.canContinue()}
				onClick={this.onClick.bind(this)}>
				<Typography className={classes.error} variant={"title"} color={"secondary"}>
					{this.state.error}
				</Typography>
				<TextField
					label="Organization name"
					className={classes.textField}
					value={this.state.name}
					onChange={e => this.setState({ name: e.target.value })}
					margin={"normal"} />
				<TextField
					label="Organization email"
					className={classes.textField}
					value={this.state.email}
					onChange={e => this.setState({ email: e.target.value })}
					margin={"normal"} />
				<TextField
					label="Password"
					className={classes.textField}
					value={this.state.password}
					onChange={e => this.setState({ password: e.target.value })}
					margin={"normal"}
					type={"password"} />
				<TextField
					label="Confirm password"
					className={classes.textField}
					value={this.state.confirmPassword}
					onChange={e => this.setState({ confirmPassword: e.target.value })}
					margin={"normal"}
					type={"password"}
					error={this.confirmPasswordError()}
					helperText={this.confirmPasswordError() ? "Passwords do not match" : ""} />
			</Onboarding>
		);
	}
}

const styles = (theme) => ({
	textField: {
		width: '100%',
		margin: theme.spacing.unit * 3
	},
	error: {
		marginTop: theme.spacing.unit * 2
	}
});

CreateOrg.propTypes = {
	setName: PropTypes.func.isRequired
};

function mapStateToProps(state) {
	return {};
}
function mapDispatchToProps(dispatch) {
	return {
		setName: (name) => dispatch({ type: SET_ORG_NAME, value: name })
	}
}

CreateOrg = connect(mapStateToProps, mapDispatchToProps)(CreateOrg);
export default withStyles(styles)(CreateOrg);
